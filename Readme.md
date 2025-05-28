# HexaSwitch - 6-Channel Switch for Tasmota

This project is a custom-designed printed circuit board (PCB) for a Tasmota-compatible IoT device based on the ESP32 microcontroller. It allows switching of **6 loads**, with each channel capable of handling up to **2 Amps**. The device contains a real-time clock such that the device can also run on an independent time base. 

<p float="left">
  <img src="img/board.png" height="250" /> 
  <img src="img/board1.jpg" height="250" />
  <img src="img/case.jpg" height="250" /> 
  <img src="img/final.jpg" height="250" /> 
</p>

I use it for switching on and off 12V valves for watering plants in the garden. It can also be used to switch relays and contactors to switch larger powers. 

---

## Features

- Link to [Schematic](schematic/schematic.pdf) and [BOM](schematic/bom/ibom.html)
- **ESP32-based** controller compatible with [Tasmota firmware](https://tasmota.github.io/)
- **6 independent load switching channels** (up to 2A per channel)
- **3 digital inputs**
- Supports power input from **5V to 24V**
- Optional **Real-Time Clock (RTC)** connector (not required for operation)
- Custom PCB designed using **KiCad**

---

## Hardware Details

- Power Supply: 5–24V DC input
- Switching: 6 channels, each capable of switching loads up to 2A
- Inputs: 3 digital inputs
- Microcontroller: ESP32
- Optional RTC interface for time-sensitive automation

---

## Usage

1. Assemble the PCB and connect loads to the output channels.
2. Flash the ESP32 with [Tasmota firmware](https://tasmota.github.io/).
3. Power the device with a DC supply between 5V and 24V.
4. Use Tasmota’s web interface or MQTT to control each channel independently.

---

## License

This project is released under the MIT License.

---



