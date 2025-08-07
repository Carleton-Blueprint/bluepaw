<div align="center">
    <img src="public/bluepaw.png" alt="Logo" width="100" height="100">

  <h2 align="center">CUBlueprint Bluepaw</h2>

  <p align="center">
    Blueprintify Profile Picture - CLI tool
  </p>
</div>

<p align="center">
  <a href="https://deepwiki.com/Carleton-Blueprint/bluepaw">
    <img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"/>
  </a>
  <a href="https://www.gnu.org/licenses/agpl-3.0">
    <img src="https://img.shields.io/badge/License-AGPL_v3-blue.svg" alt="License: AGPL v3"/>
  </a>
</p>

Bluepaw is a Python command-line tool that takes a profile picture and some background images to create a blueprint-styled profile picture. The tool intelligently separates the foreground (the subject) and background, applies a grayscale effect, and merges them with user-defined streak patterns to create a unique and stylized final image.

## Features ✨

**Automatic Foreground/Background Separation:** It automatically separates the main subject (foreground) from the background of the input image.

**Blueprint-style Grayscale:** The tool applies a grayscale effect to both the foreground and background, giving them a blueprint-like appearance.

**Customizable Streaks:** Users can provide custom images to use as background and optional foreground "streaks" to add a creative flair to the final output.

Installation 💻
To use this tool, you'll need Python 3.7+. The project relies on several external libraries. You can install them using pip:

```Bash
pip install rembg
```

## Usage 🚀

The tool is run from the command line and requires an input image and a background streak image. An optional foreground streak image can also be provided.

```Bash
python bluepaw -h
```

### Command-line Arguments

- `image_path`: Path to the profile picture you want to convert.

- `streak_bg_path`: Path to the image file to be used as the background streak pattern.

- `streak_fg_path` (optional): Path to an image to be used as a foreground streak. This is useful for adding an extra layer of detail.

- `-o` or `--output`: The name of the output file. Defaults to out.png.

### Example

Here's an example of how to run the tool:

```Bash
python bluepaw my_profile_pic.png streak_bg.png -o my_blueprint_profile.png
```

### Screenshots

### License

Bluepaw is distributed under [AGPL-3.0.only](LICENSE.md).
