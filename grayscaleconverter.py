import cv2
import matplotlib.pyplot as plt

def convert_to_grayscale(input_path):
    image = cv2.imread(input_path)
    
    if image is None:
        print(f"Error: Could not read image from {input_path}")
        return None
    
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(gray_image, cmap='gray')
    plt.title("Grayscale Image")
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    
    output_path = "grayscale_output.jpg"
    cv2.imwrite(output_path, gray_image)
    print(f"Grayscale image saved as: {output_path}")
    
    return gray_image

if __name__ == "__main__":
    image_path = input("Enter the path to your image: ").strip()
    image_path = image_path.strip('"\'')
    result = convert_to_grayscale(image_path)
    
    if result is not None:
        print("Conversion completed successfully!")