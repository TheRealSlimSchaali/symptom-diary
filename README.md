# Symptom Diary

## Overview

The **Symptom Diary** custom component for Home Assistant allows you to track fever and medication for your family. It enables you to log temperature measurements along with timestamps and the medication given, making it easier to monitor health conditions.

## Features

- Log temperature measurements with timestamps.
- Record which medication was given for each measurement.
- Easy integration with Home Assistant.

## Installation

### Prerequisites

- Home Assistant installed and running.
- HACS (Home Assistant Community Store) installed.

### Steps

1. **Add the Repository to HACS**:
   - Open HACS in your Home Assistant interface.
   - Go to the "Integrations" tab.
   - Click on the three dots in the top right corner and select "Custom repositories".
   - Enter the following URL: `https://github.com/yourusername/symptom_diary` and select "Integration" as the category.
   - Click "Add".

2. **Install the Component**:
   - After adding the repository, search for "Symptom Diary" in the Integrations page.
   - Click on it and then click the "Install" button.

3. **Configure the Component**:
   - Add the following configuration to your `configuration.yaml` file:

   ```yaml
   sensor:
     - platform: symptom_diary
   ```

4. **Restart Home Assistant**:
   - Restart Home Assistant to load the new custom component.

## Usage

Once installed and configured, you can start logging temperature measurements and medications through the Home Assistant interface. The sensor will display the latest temperature and store the history of measurements.

## Contributing

If you would like to contribute to this project, feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Home Assistant community for their support and resources.
