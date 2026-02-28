import cv2
import matplotlib.pyplot as plt

def resize_image(input_path, new_width, new_height):
    image = cv2.imread(input_path)
    if image is None:
        print(f"Error: Could not read image from {input_path}")
        return None
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w = image.shape[:2]
    print(f"Original image size: {w} x {h} pixels")
    resized_image = cv2.resize(image, (new_width, new_height))
    print(f"Resized image size: {new_width} x {new_height} pixels")
    resized_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title(f"Original: {w} x {h}")
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(resized_rgb)
    plt.title(f"Resized: {new_width} x {new_height}")
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    output_path = "resized_output.jpg"
    cv2.imwrite(output_path, resized_image)
    print(f"Resized image saved as: {output_path}")
    
    return resized_image

if __name__ == "__main__":
    image_path = input("Enter the path to your image: ").strip()
    image_path = image_path.strip('"\'')
    
    try:
        new_width = int(input("Enter new width in pixels: "))
        new_height = int(input("Enter new height in pixels: "))
        result = resize_image(image_path, new_width, new_height)
        
        if result is not None:
            print("Resizing completed successfully!")
            
    except ValueError:
        print("Error: Please enter valid numbers for width and height")