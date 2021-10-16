import cv2
import orien_lines_practice
# ( width * height  ===> x , y  )
framewidth = 500  # image width and height params
frameheight = 400


# requirement to draw safe line
# input("Enter the orientation of hand progression ~ lr,rl,bt,tb :")
Orientation = 'lr'
Line_Perc1 = float(15)
Line_Perc2 = float(30)


def show_raw_image(img_path,framewidth=500,frameheight=400):
    try:
        img = cv2.imread(filename=img_path)
        img = cv2.resize(img, (framewidth, frameheight))
        cv2.imshow(winname='originalImage', mat=img)
        cv2.waitKeyEx(delay=0)
    except Exception as e:
        raise e

def get_raw_img_array(img_path,framewidth=500,frameheight=400):
    try:
        img = cv2.imread(filename=img_path)
        img = cv2.resize(img ,(framewidth, frameheight))
        return img, img.shape
    except Exception as e:
        print(f'{str(e)} : Exception occures at fun get_raw_img_array ..')
        raise e







if __name__ == '__main__':
    filepath = 'rough_work/orientation/images/connecting-mogo-with-project.png'
    storage_path = 'rough_work/orientation/output_images/img2'
    raw_img_array = get_raw_img_array(img_path=filepath)[0]
    #show_raw_image(img_path=filepath)
    print(raw_img_array , raw_img_array.shape)
    print(f"raw_img_array.shape[1] ={raw_img_array.shape[1]}" )

    # let's time to draw line on img
    # input("Enter the orientation of hand progression ~ lr,rl,bt,tb :")
    Orientation = 'bt'
    Line_Perc1 = float(15)
    Line_Perc2 = float(30)
    orien_lines_practice.drawsafelines(image_np=raw_img_array,Orientation=Orientation,
                                       Line_Perc1=Line_Perc1 , Line_Perc2=Line_Perc2 ,
                                       store_img_path=None)

    # orien_lines_practice.drawsafelines(image_np=raw_img_array, Orientation='bt',
    #                                    Line_Perc1=Line_Perc1, Line_Perc2=Line_Perc2,
    #                                    store_img_path=storage_path + 'orientation_bt.png'
    #                                    )
    # orien_lines_practice.drawsafelines(image_np=raw_img_array, Orientation='rl',
    #                                    Line_Perc1=Line_Perc1, Line_Perc2=Line_Perc2 ,
    #                                    store_img_path=storage_path + 'orientation_rl.png'
    #                                    )
    # orien_lines_practice.drawsafelines(image_np=raw_img_array, Orientation='lr',
    #                                    Line_Perc1=Line_Perc1, Line_Perc2=Line_Perc2 ,
    #                                    store_img_path=storage_path + 'orientation_lr.png'
    #




