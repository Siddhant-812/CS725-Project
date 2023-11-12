import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import pandas as pd

def plot_customized_bounding_boxes(df, box_width=1, box_color='r'):
    unique_images = df['image_name'].unique()

    for image_name in unique_images:
        image_df = df[df['image_name'] == image_name]
        img = Image.open(image_name)
        fig, ax = plt.subplots(1)
        ax.imshow(img)

        for _, row in image_df.iterrows():
            object_name = row['object_name']
            x_center = row['x']
            y_center = row['y']
            width = row['w']
            height = row['h']
            confidence = row['conf']

            # Calculate bounding box coordinates
            x = (x_center - width / 2) * img.width
            y = (y_center - height / 2) * img.height
            width *= img.width
            height *= img.height

            rect = patches.Rectangle((x, y), width, height,
                linewidth=box_width, edgecolor=box_color, facecolor='none')
            ax.add_patch(rect)

            label = f"{object_name} {confidence:.2f}"
            ax.text(x, y, label, color=box_color, verticalalignment='top')

        plt.title(f'Bounding Boxes for {image_name}')
        plt.show()

df = pd.DataFrame(index=[0, 1], columns=['image_name', 'object_id', 'object_name', 'x', 'y', 'w', 'h', 'conf'])
df.iloc[0, :] = ['/Users/soumen/Desktop/IITB/CS725-FML-Project/yolo_demo/images/testing/apple015S(1).jpg',
                 0, 'apple', 0.6054, 0.5505, 0.2718, 0.3236, 0.9763]
df.iloc[1, :] = ['/Users/soumen/Desktop/IITB/CS725-FML-Project/yolo_demo/images/testing/apple015S(1).jpg',
                 1, 'coin', 0.1960, 0.6860, 0.0837, 0.1041, 0.8784]
plot_customized_bounding_boxes(df, box_width=2, box_color='b')
