import cv2
import time
from opencv_utils import draw_text, load_classes, load_colors, draw_detection

def main():
    # Load YOLOv4 Tiny model
    weights_path = "E:\\MAGANG\\Project_iSense\\weights\\yolov4-tiny-416x416_best.weights"
    cfg_path = "E:\\MAGANG\\Project_iSense\\cfg\\yolov4-tiny-416x416.cfg"
    
    net = cv2.dnn.readNet(weights_path, cfg_path)

    # Load classes (obj.names file)
    classes = load_classes("E:\\MAGANG\\iSense\\data\\obj.names")

    # Load class colors
    class_colors = load_colors(classes)

    # # Set the address of the DroidCam video stream
    # droidcam_url = 'http://192.168.100.16:4747/video'

    # # Open DroidCam video stream
    # cap = cv2.VideoCapture(droidcam_url)
    
    # Open webcam
    cap = cv2.VideoCapture(1)

    # Set the desired display resolution for the webcam
    display_width = 800
    display_height = 600

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # You can change the codec as needed
    output_video_path = "output_webcam.mp4"  # Set your desired output video file path
    out = cv2.VideoWriter(output_video_path, fourcc, 20.0, (display_width, display_height))

    frame_count = 0
    start_time = time.time()

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        if not ret:
            break  # Break the loop if no more frames are available

        # Resize the frame to the desired display resolution
        resized_frame = cv2.resize(frame, (display_width, display_height))

        # Prepare the resized frame for inference
        blob = cv2.dnn.blobFromImage(resized_frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)

        # Get output layer names
        output_layer_names = net.getUnconnectedOutLayersNames()

        # Perform inference
        detections = net.forward(output_layer_names)

        # Process and display the detections
        resized_frame, num_person_detections, num_head_detections = draw_detection(resized_frame, classes, class_colors, detections, confidence_threshold=0.5)

        # Calculate and display fps
        frame_count += 1
        elapsed_time = time.time() - start_time
        fps = frame_count / elapsed_time

        # Display the result with bounding box count and fps
        person_label = f'Person: {num_person_detections}'
        head_label = f'Head: {num_head_detections}'
        fps_label = f'FPS: {fps:.2f}'

        # Draw hologram effect for the "Person" text
        draw_text(resized_frame, person_label, (10, 30), (0, 255, 0))

        # Draw hologram effect for the "Head" text
        draw_text(resized_frame, head_label, (10, 70), (0, 255, 0))

        # Draw hologram effect for the "FPS" text
        draw_text(resized_frame, fps_label, (10, 110), (0, 255, 0))

        # Write the frame to the output video file
        out.write(resized_frame)

        # Show the resized frame with normal window properties
        cv2.imshow("YOLOv4 Tiny Crowd Detection", resized_frame)

        # Resize the OpenCV window
        cv2.resizeWindow("YOLOv4 Tiny Crowd Detection", display_width, display_height)

        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Calculate and display the average FPS
    average_fps = frame_count / (time.time() - start_time)
    print(f"Average FPS: {average_fps}")

    # Release the video capture object, release the VideoWriter object, and close the window
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
