# EuroPi hardware (Semi-Sensible Synth THT KiCad remix)

This version of EuroPi is a remix with some small changes.

## Differences / changes from stock EuroPi

- Input jacks at bottom, above output jacks
- Uses 14mm high, 6x6mm base tactile buttons with ~6.1-6.2mm diameter plastic caps.
- Uses a 38mm OLED, commonly sold on AliExpress (mounted slightly offset from centre for your OCD)
- Has a bodge zone with some extra holes and exposed pads for cutting traces and re-routing the OLED pins if yours doesn’t follow the ‘CPC’-style pinout (less elegant than the original EuroPi rerouting holes, but intended as a last resort if you happen to have another OLED that still fits)
- Has optional non-electrical pin header to help support the other end of the OLED
- No standoff screw joining boards, extra pin headers at bottom instead
- General re-routing and component position tweaks to make it all work.

## BOM variations of note

- 0.91” OLED (38mm wide, GND/VCC/SCL/SDA): [Ali Express](https://www.aliexpress.com/item/32672229793.html)
- 6x6x14 mm tactile buttons: [Ali Express](https://www.aliexpress.com/item/32960657626.html)
- Tactile button caps: [Ali Express (white)](https://www.aliexpress.com/item/32872180785.html), [Ali Express (black)](https://www.aliexpress.com/item/32873394381.html)

These are common parts across various sellers, so should be relatively easy to find at a good price.

## v0.10.0-sss-tht TODO notes

I have ordered and built a module using the `v0.10.0-sss-tht` production files and it works.
These are some minor changes I would make in a revision.

- Add more component value labels to silkscreen, especially to resistors
- Add + to LED silkscreen
- LED panel holes could be a little smaller (~0.4mm diameter smaller)
- Consider adding pin headers between the front panel and PCB, above the OLED to better secure when using nut-less trimmer pots.
  - _(This would be a female header above the OLED and an SMD right angle male header on exposed pads on the back of the front panel - or get fancy with a solderable standoff like https://www.adafruit.com/product/4207)_
- Build guide: 
  - Solder the I2C header before Pico & power header (tricky otherwise)
  - Solder the bottom centre jack (J5) before bottom board joiner on the opposite side of the board (if using 8x1 with two middle pins removed as joiner). If you forget, it can be soldered from the opposite side of the board.
  - I had to glue my button caps on to the tactile buttons - not a big deal, but I expected them to attach via friction
  - I used small plastic trimmer pots in my first build, however it’s better to use proper metal pots with nuts. This is because without pot nuts, pressing the buttons too hard flexes the PCB away from the front panel. Using [trimmer knobs](https://www.aliexpress.com/item/1005002336855641.html) also help.


# Hardware Specifications

## Outputs
- 1k Output Impedance
- RC filter smoothed PWM
- ~1.5kHz Maximum usable frequency (without changing RC values)
- 0.000176V Maximum ripple peak-to-peak
- 0.0108s Settle time from 0% to 90% duty cycle
- 0-10V

## Analogue Input
- 100k Input Impedance
- 0-12V Readable Range
- Protected for ±36V (TL074 limits, MCP6002 will always clip to ±3.3V)

## Digital Input
- 100k Input Impedance
- 0.8V threshold to read as high

## OLED
- SSD1306 0.91"
- 128 x 32 pixels
- I2C Protocol
