"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.helpers.entity import async_update_entity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
import logging

_LOGGER = logging.getLogger(__name__)


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the sensor platform."""
    add_entities([SymptomDiarySensor()])



class SymptomDiarySensor(SensorEntity):
    """Representation of a Symptom Diary Sensor."""

    def __init__(self, coordinator: DataUpdateCoordinator):
        """Initialize the sensor."""
        self.coordinator = coordinator
        self._attr_name = "Symptom Diary Temperature"
        self._attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
        self._attr_state_class = "measurement"  # Use the appropriate state class
        self._attr_device_class = "temperature"  # Use the appropriate device class
        self._attr_unique_id = "symptom_diary_temperature"  # Unique ID for the sensor

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get("temperature")  # Adjust based on your data structure

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return {
            "medication": self.coordinator.data.get("medication"),  # Example attribute
            "timestamp": self.coordinator.data.get("timestamp"),  # Example attribute
        }

    async def async_update(self):
        """Fetch new state data for the sensor."""
        await self.coordinator.async_request_refresh()  # Refresh data from the coordinator