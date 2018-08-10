# Quindar Tones

Generate tones on keypress including:

- [Quindar tones](https://en.wikipedia.org/wiki/Quindar_tones)
  used by NASA for decades as in-band PTT signaling
- Motorola tone remote
- Nextel PTT chirp

## Install

```sh
pip install -e .
```

## Usage
```sh
keytones
```

-   left-arrow: 2525 Hz
-   right-arrow: 2475 Hz
-   up-arrow: tone remote leadin 2175 1950 Hz
-   down-arrow: Nextel chirp 1800 Hz bips
