import cv2


def show_img(img_array):
    cv2.imshow(winname='img after orientation line plot' , mat=img_array)
    print('Drawing the line on image and ready to show ')
    cv2.waitKey(0)

def store_img(wheretostore  , img_array):
    '''
    Args:
        wheretostore: where you want to store img
        img_array: image_array

    Returns:Nothing
    '''
    cv2.imwrite(filename=wheretostore ,img=img_array)
    print(f"Img stored at Loc{wheretostore}")


def drawsafelines(image_np,Orientation,Line_Perc1,Line_Perc2 , store_img_path = None):
    '''
     THis method will draw  Safe lines on the images ..
     as per Orientation Given and the linprec1 and 2
    Args:
        image_np: image array
        Orientation:  lr,rl,bt,tb
        Line_Perc1: float(number)
        Line_Perc2:float(number)


    Returns: img & orientation points
    '''
    # x = width = image_np.shape[0]
    # y = height = image_np.shape[1]
    # calculations : (400 , 500 )
    # possi = 500 - 500/3 = 334   , org=  (334,30)

    posii=int(image_np.shape[1]-(image_np.shape[1]/3))
    cv2.putText(image_np,'Blue Line :Safety Border Line',
                        (posii,30),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (255,0,0),0, cv2.LINE_AA)
    cv2.putText(image_np, 'Red Line : Machine Border Line  ',
                        (posii,50),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0,0,255), 1, cv2.LINE_AA)
    
    if(Orientation=="bt"):
        # For Orientation = bottom > top
        # calculation : x = shape[0] = 400 , y = shape[1] = 600
        # line_position1 = shape[0]*(10/100) = 400 * 0.15 = 60  ( plot machine border (red) line at 40 from top )
        # line_position2 = shape[0]*(30/100) = 400 * 0.3 = 120 ( plot safety border (blue) line at 120 from top )
        # so the distance between two line ( red & blue is ) = 120-60 = 60
        # this distance will change as per use-case , here we're considering 60
        Line_Position1=int(image_np.shape[0]*(Line_Perc1/100))     # 60
        Line_Position2=int(image_np.shape[0]*(Line_Perc2/100))     # 120

        # we're plotting line by taking reference of top
        # pt1 = ( x1,y1) pt2 = (x2 , y2) => (0,60) ( 600,60 ) <- for line1 ( red - Machine borderline)
        # pt1 , pt2  = (0,120)(600,120)  <- for  line 2 (blue safety line )

        cv2.line(img=image_np, pt1=(0, Line_Position1), pt2=(image_np.shape[1], Line_Position1),
                                    color=(0, 0, 255), thickness=2, lineType=8, shift=0)
        cv2.line(img=image_np, pt1=(0, Line_Position2), pt2=(image_np.shape[1], Line_Position2),
                                    color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        show_img(img_array=image_np)
        if store_img_path :
            store_img(wheretostore=store_img_path , img_array=image_np)
        else:
            pass
        return Line_Position2
        
    elif(Orientation=="tb"):
        # For Orientation = top -> bottom
        # calculation : x = shape[0] = 400 , y = shape[1] = 600
        # pos1  = x - (x*0.15) = 400 - 400 *.15 = 340
        # pos2 =  x - (x*0.15) = 400 - 400 *.30 = 280

        Line_Position1=int(image_np.shape[0]-(image_np.shape[0]*(Line_Perc1/100)))
        Line_Position2=int(image_np.shape[0]-(image_np.shape[0]*(Line_Perc2/100)))

        # we're plotting line by taking reg of top
        # pt1 = ( x1,y1) pt2 = (x2 , y2) => (0,340) ( 600,340 ) <- for line1 ( red - Machine borderline)
        # pt1 , pt2  = (0,280)(600,280)  <- for  line 2 (blue safety line )
        cv2.line(img=image_np, pt1=(0, Line_Position1), pt2=(image_np.shape[1], Line_Position1),
                 color=(0, 0, 255), thickness=2, lineType=8, shift=0)
        cv2.line(img=image_np, pt1=(0, Line_Position2), pt2=(image_np.shape[1], Line_Position2),
                 color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        show_img(img_array=image_np)
        if store_img_path :
            store_img(wheretostore=store_img_path , img_array=image_np)
        else:
            pass
        return Line_Position2
    
    elif(Orientation=="lr"):
        # if orientation is changes then ( height and width will be altered )
        # For Orientation = left -> right
        # calculations : x, y= 600 , 400 ( altered due to orientation change )
        # pos1 = y - y * 0.15 = 400 - 400*0.15 =340
        # pos2 = y - y * 0.30 = 400 - 400*0.30 =280
        Line_Position1=int(image_np.shape[1]-(image_np.shape[1]*(Line_Perc1/100)))
        Line_Position2=int(image_np.shape[1]-(image_np.shape[1]*(Line_Perc2/100)))

        # we're plotting line by taking reference of left
        # pt1 = ( x1,y1) pt2 = (x2 , y2) => (pos1,0) ( pos1 ,x )
        #      => ( 340 , 0 ) (340,600) (<- for line1 ( red - Machine borderline)
        # pt1 , pt2  => (280,0) (280,600) (<- for line2 ( blue - safety borderline)


        cv2.line(img=image_np, pt1=(Line_Position1, 0), pt2=(Line_Position1,image_np.shape[0]),
                 color=(0, 0, 255), thickness=2, lineType=8, shift=0)
        cv2.line(img=image_np, pt1=(Line_Position2, 0), pt2=(Line_Position2,image_np.shape[0]),
                 color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        show_img(img_array=image_np)
        if store_img_path :
            store_img(wheretostore=store_img_path , img_array=image_np)
        else:
            pass
        return Line_Position2
        
        
    elif(Orientation=="rl"):
        # For Orientation =right > left
        # if orientation is changes then ( height and width will be altered )
        # calculations : x, y= 600 , 400 ( altered due to orientation change )
        # pos1 = y - y * 0.15 = 400 - 400*0.15 =340
        # pos2 = y - y * 0.30 = 400 - 400*0.30 =280

        Line_Position1=int(image_np.shape[1]*(Line_Perc1/100))
        Line_Position2=int(image_np.shape[1]*(Line_Perc2/100))

        # we're plotting line by taking reference of right
        # pt1 = ( x1,y1) pt2 = (x2 , y2) => (pos1,0) ( pos1 ,x )
        #      => ( 340 , 0 ) (340,600) (<- for line1 ( red - Machine borderline)
        # pt1 , pt2  => (280,0) (280,600) (<- for line2 ( blue - safety borderline)

        cv2.line(img=image_np, pt1=(Line_Position1, 0), pt2=(Line_Position1,image_np.shape[0]),
                 color=(0, 0, 255), thickness=2, lineType=8, shift=0)
        cv2.line(img=image_np, pt1=(Line_Position2, 0), pt2=(Line_Position2,image_np.shape[0]),
                 color=(255, 0, 0), thickness=2, lineType=8, shift=0)
        show_img(img_array=image_np)
        if store_img_path :
            store_img(wheretostore=store_img_path , img_array=image_np)
        else:
            pass
        return Line_Position2
    else:
        print('some error happens : please Provide the Orientation.....')
