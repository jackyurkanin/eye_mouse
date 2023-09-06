# eye_mouse

    an application for windows that allows for your eyes to act as your computers mouse.

# MVP

1. Machine Vision - eye detection and monitoring
2. Application for windows that has permissions of a mouse.
3. eye to screen translation. need to calculate distance between person and screen. and camera to screen corner

# machine vision

- detect eyes using openCV.
- single eye closed detection based on previous eye locations.
- returns state of eyes with 1 (open) or 0 (closed)

- potentially learn where a person is looking based on real-time training
  - random dot generator and look at the dot and hit a button
  - train the model with location of dot and eye imageS

# Windows Application

# Eye2Screen

- calibration angle of eyes with respect to corner in x and y axis
