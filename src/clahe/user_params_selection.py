
def user_params_selection(): 
    clipLimit = input("Choose Threshold for contrast limiting(Default = 2.0):\n")
    clipLimit = float(clipLimit)
    n = input("Size of grid for histogram equalization.\nDefines the number of tiles in row and column(Default =8 => (8,8)):\n")
    tileGridSize=(int(n),int(n))
    return clipLimit,tileGridSize