import unittest
from unittest.mock import patch

from src.contracts import BUOY_CONTRACT, MARINE_CONTRACT, TIDE_CONTRACT
from src.core.orchestrator import run_command_center
from src.services.marine_service import (
    get_marine_conditions,
    get_simulated_marine_conditions,
)
from src.services.species_engine import calculate_species_scores
from src.system_validator import validate_contract
from src.telemetry_engine import build_telemetry


class ContractValidationTests(unittest.TestCase):

    def test_marine_contract_fills_missing_nested_defaults(self):

        validated = validate_contract(
            {
                "sea_state": {
                    "wave_height_ft": 2.5
                }
            },
            MARINE_CONTRACT
        )

        self.assertEqual(
            validated["sea_state"]["wave_height_ft"],
            2.5
        )
        self.assertEqual(
            validated["sea_state"]["swell_direction"],
            "UNKNOWN"
        )
        self.assertEqual(
            validated["wind"]["speed_mph"],
            0
        )

    def test_tide_contract_preserves_legacy_and_canonical_keys(self):

        sample = {
            "current": {
                "time": "2026-06-13 00:00",
                "height": 1.2,
                "height_ft": 1.2,
                "direction": "INCOMING",
                "velocity": "MODERATE",
            },
            "tidal_range": 2.4,
            "tidal_range_ft": 2.4,
            "slack_windows": [],
            "tides": [],
        }

        validated = validate_contract(
            sample,
            TIDE_CONTRACT
        )

        self.assertEqual(
            validated["current"]["height_ft"],
            1.2
        )
        self.assertEqual(
            validated["tidal_range_ft"],
            2.4
        )
        self.assertEqual(
            validated["tidal_range"],
            2.4
        )


class TelemetryNormalizationTests(unittest.TestCase):

    def test_buoy_regional_fields_map_to_canonical_contract(self):

        fake_marine = {
            "wave_height": 9.9,
            "wave_period": 3.3,
        }
        fake_buoy = {
            "regional_wave_height_ft": 2.4,
            "regional_swell_period_sec": 8.1,
            "regional_wind_speed_kt": 12,
            "regional_rating": "GOOD",
            "stations_active": 2,
        }

        with patch(
            "src.telemetry_engine.get_marine_conditions",
            return_value=fake_marine
        ), patch(
            "src.telemetry_engine.get_regional_marine_data",
            return_value=fake_buoy
        ):
            telemetry = build_telemetry()

        validated = validate_contract(
            telemetry,
            BUOY_CONTRACT
        )

        self.assertEqual(
            validated["regional"]["wave_height_ft"],
            2.4
        )
        self.assertEqual(
            validated["regional"]["wave_period_sec"],
            8.1
        )
        self.assertEqual(
            validated["regional"]["wind_speed_kt"],
            12
        )
        self.assertEqual(
            validated["regional"]["rating"],
            "GOOD"
        )
        self.assertEqual(
            validated["stations"]["active"],
            2
        )


class SimulatedMarineQuarantineTests(unittest.TestCase):

    def test_simulated_marine_provider_marks_payload_as_simulated(self):

        payload = get_simulated_marine_conditions()

        self.assertEqual(
            payload["source_type"],
            "simulated"
        )
        self.assertTrue(
            payload["is_simulated"]
        )
        self.assertTrue(
            payload["_meta"]["is_simulated"]
        )

    def test_legacy_marine_alias_preserves_simulation_metadata(self):

        payload = get_marine_conditions()

        self.assertEqual(
            payload["source_type"],
            "simulated"
        )
        self.assertTrue(
            payload["is_simulated"]
        )


class OrchestratorPayloadTests(unittest.TestCase):

    def test_orchestrator_exposes_canonical_and_dashboard_marine_payloads(self):

        canonical_marine = {
            "sea_state": {
                "wave_height_ft": 2.5,
                "wave_period_sec": 7,
                "swell_height_ft": 2.0,
                "swell_period_sec": 8,
                "swell_direction": "E",
            },
            "wind": {
                "speed_mph": 10,
                "direction": "E",
            },
            "forecast": {
                "headline": "Test",
                "details": "Test forecast",
            },
            "advisories": [],
        }
        system = {
            "marine": canonical_marine,
            "tides": {
                "current": {
                    "direction": "INCOMING",
                    "velocity": "MODERATE",
                    "height_ft": 1.1,
                },
                "tidal_range_ft": 2.2,
                "slack_windows": [],
                "tides": [],
            },
            "buoys": {
                "regional": {
                    "wave_height_ft": 2.4,
                    "wave_period_sec": 8.1,
                    "wind_speed_kt": 12,
                    "rating": "GOOD",
                },
                "stations": {
                    "active": 2,
                },
            },
            "risk": {
                "danger_score": 20,
                "risk_state": "LOW",
                "launch_viability": "GOOD",
                "standing_wave_risk": False,
                "summary": [],
            },
            "prediction": {
                "feeding_score": 70,
                "activity": "HIGH",
                "species": {},
                "primary_target": "MAHI",
                "primary_score": 75,
            },
            "tactical": {
                "mission_status": "MONITOR",
                "primary_target": "MAHI",
                "confidence": 74,
            },
            "synthesis": {},
        }
        simulated = {
            "source_type": "simulated",
            "is_simulated": True,
            "wind_speed": 12,
            "wind_direction": 90,
            "wave_height": 2.1,
            "wave_period": 7,
            "water_temp": 80,
            "pressure": 1015,
            "moon_phase": "Full Moon",
            "tide_state": "Incoming",
            "visibility": 8,
            "timestamp": "12:00:00",
        }

        with patch(
            "src.core.orchestrator.build_marine_system",
            return_value=system
        ), patch(
            "src.core.orchestrator.get_simulated_marine_conditions",
            return_value=simulated
        ), patch(
            "src.core.orchestrator.store_snapshot"
        ), patch(
            "src.core.orchestrator.get_recent_snapshots",
            return_value=[]
        ):
            payload = run_command_center()

        self.assertEqual(
            payload["canonical_marine"],
            canonical_marine
        )
        self.assertTrue(
            payload["marine"]["is_simulated"]
        )
        self.assertTrue(
            payload["dashboard_marine"]["is_simulated"]
        )
        self.assertFalse(
            payload["telemetry_meta"]["canonical_marine"]["is_simulated"]
        )
        self.assertTrue(
            payload["telemetry_meta"]["dashboard_marine"]["is_simulated"]
        )
        self.assertIn(
            "alerts",
            payload["tactical"]
        )


class SpeciesEngineCompatibilityTests(unittest.TestCase):

    def test_species_service_returns_sorted_list_from_registry(self):

        registry_results = {
            "SNAPPER": {
                "species": "SNAPPER",
                "score": 64,
            },
            "MAHI": {
                "species": "MAHI",
                "score": 82,
            },
        }

        with patch(
            "src.services.species_engine.run_species_engines",
            return_value=registry_results
        ):
            results = calculate_species_scores(
                {},
                {},
                {},
                {}
            )

        self.assertEqual(
            [
                item["species"]
                for item in results
            ],
            [
                "MAHI",
                "SNAPPER",
            ]
        )


if __name__ == "__main__":
    unittest.main()
