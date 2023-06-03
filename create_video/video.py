import cv2, os

def make_video():
    out = cv2.VideoWriter("/home/arthur/Documents/code/it-solution/video.mov", 
                        cv2.VideoWriter_fourcc('M','J','P','G'), 50.0, (100, 100)) 
    filenames = [int(path.split('_')[1].split('.')[0]) for path in 
                 os.listdir(r'/home/arthur/Documents/code/it-solution/images')]
    filenames.sort()
    for filename in filenames:
        out.write(cv2.imread
                  (f'/home/arthur/Documents/code/it-solution/images/image_{filename}.png'))
    out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    make_video()
