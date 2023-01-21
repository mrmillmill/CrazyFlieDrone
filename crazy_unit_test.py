import unittest
from unittest.mock import MagicMock

class TestLedRingHelper(unittest.TestCase):
    def test_set_value(self):
        # Create a mock object for the SyncCrazyflie class
        mock_cf = MagicMock()

        # Test the headlightsOn function
        LedRingHelper.headlightsOn(mock_cf)
        mock_cf.param.set_value.assert_called_with("ring.headlightEnable", "1")

        # Test the setRingEffect function
        LedRingHelper.setRingEffect(mock_cf, "test_style")
        mock_cf.param.set_value.assert_called_with("ring.effect", "test_style")

        # Test the setRingColorMaxWhite function
        LedRingHelper.setRingColorMaxWhite(mock_cf)
        mock_cf.param.set_value.assert_any_call("ring.solidRed", "255")
        mock_cf.param.set_value.assert_any_call("ring.solidGreen", "255")
        mock_cf.param.set_value.assert_any_call("ring.solidBlue", "255")

        # Test the setRingColorMidWhite function
        LedRingHelper.setRingColorMidWhite(mock_cf)
        mock_cf.param.set_value.assert_any_call("ring.solidRed", "63")
        mock_cf.param.set_value.assert_any_call("ring.solidGreen", "63")
        mock_cf.param.set_value.assert_any_call("ring.solidBlue", "63")

        # Test the setRingColorMinWhite function
        LedRingHelper.setRingColorMinWhite(mock_cf)
        mock_cf.param.set_value.assert_any_call("ring.solidRed", "31")
        mock_cf.param.set_value.assert_any_call("ring.solidGreen", "31")
        mock_cf.param.set_value.assert_any_call("ring.solidBlue", "31")

        # Test the setRingColorOff function
        LedRingHelper.setRingColorOff(mock_cf)
        mock_cf.param.set_value.assert_any_call("ring.solidRed", "0")
        mock_cf.param.set_value.assert_any_call("ring.solidGreen", "0")
        mock_cf.param.set_value.assert_any_call("ring.solidBlue", "0")

        # Test the setRingWhiteBrightness function
        LedRingHelper.setRingWhiteBrightness(mock_cf, 200)
        mock_cf.param.set_value.assert_any_call("ring.solidRed", "200")
        mock_cf.param.set_value.assert_any_call("ring.solidGreen", "200")
        mock_cf.param.set_value.assert_any_call("ring.solidBlue", "200")

        LedRingHelper.setRingWhiteBrightness(mock_cf, -100)
        mock_cf.param.set_value.assert_
