**dreamer** - Music Visualization Tool
====================================

Transform your music into visual experiences with **dreamer**. This Python tool analyzes audio files using advanced signal processing to generate synchronized video visualizations, creating dynamic animations that respond to your music's rhythm, frequency content, and energy.

Key Features:
- Mel spectrogram analysis for frequency visualization
- RMS energy tracking for dynamic animations
- Real-time audio processing with librosa
- Customizable visual effects and animations
- Easy-to-use command line interface


Features
--------

- Audio Analysis
    - Mel spectrogram generation for frequency visualization
    - RMS energy tracking for amplitude analysis
    - Real-time audio processing with librosa
- Visualization
    - Dynamic video generation synchronized to music
    - Customizable visual effects and animations
    - High-quality MP4 output
- Easy Integration
    - Simple command-line interface
    - Python API for programmatic usage
    - Flexible input format support

Installation
------------

You can install **dreamer** using pip:

.. code-block:: bash

   pip install harmonic-resonance-dreamer

Usage
-----



After installation, you can use the ``dreamer`` command to create a new project:

.. code-block:: bash

   dreamer 

The basic command to generate a visualization is:

.. code-block:: bash

   dreamer <audio_file>

Where <audio_file> is the path to your audio file (supports WAV format).

Dependencies
------------

**dreamer** depends on the following Python packages:

- textual: Terminal user interface framework
- rich: Terminal formatting and styling
- jinja2: Template engine
- librosa: Audio processing library
- matplotlib: Plotting and visualization
- numpy: Numerical computing

Contributing
------------

Contributions are welcome! Please see our [GitHub issues](https://github.com/harmonic-resonance/dreamer/issues) for ways to contribute.

License
-------

**dreamer** is licensed under the MIT License. See the `LICENSE` file for more details.
