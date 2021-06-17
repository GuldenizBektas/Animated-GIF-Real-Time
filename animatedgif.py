# import libraries
import cv2 as cv # image operations
import imageio # to save the images stored in the array and turn them into a gif file

"""
0 is the main camera. If you have an external camera, try with 1.
"""
# get image
cap = cv.VideoCapture(0)

# we'll save the images to frames list variable.
frames = []
image_count = 0

"""
pressing 'a' -> saving the images
pressing 'q' -> killing the camera, and all operations
"""

# take the frame from real time
while True:

    ret, frame = cap.read()

    cv.imshow("frame", frame)

    key = cv.waitKey(0)
    if key == ord("a"):
        image_count += 1
        frames.append(frame)
        print("Adding new image:", image_count)
    elif key == ord("q"):
        break

print("Images added: ", len(frames))

# save gif aniamation
print("Saving GIF file...")
with imageio.get_writer("tenth.gif", mode = "I") as writer:
    for idx, frame in enumerate(frames):
        print("Adding frame to GIF file: ", idx + 1)
        # without this part our images will be in BGR format, we want RGB
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        writer.append_data(rgb_frame)

cap.release()
cv.destroyAllWindows()