from PIL import Image
import os

def resize_image(input_path, output_path, max_width=1200):
    try:
        if not os.path.exists(input_path):
            print(f"Error: {input_path} not found.")
            return

        with Image.open(input_path) as img:
            # Convert to RGB if necessary
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # Calculate new height to maintain aspect ratio
            width, height = img.size
            if width > max_width:
                ratio = max_width / width
                new_height = int(height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                print(f"Resized from {width}x{height} to {max_width}x{new_height}")
            else:
                print(f"Image width ({width}) is smaller than max_width ({max_width}). No resizing needed.")

            # Save with optimization
            img.save(output_path, "JPEG", quality=85, optimize=True)
            print(f"Saved optimized image to {output_path}")
            
            # Check file size
            file_size = os.path.getsize(output_path)
            print(f"New file size: {file_size / 1024:.2f} KB")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = "pedida76de97.jpg"
    output_file = "preview.jpg"
    resize_image(input_file, output_file)
