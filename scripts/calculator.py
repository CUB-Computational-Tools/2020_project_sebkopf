"""
This function predicts the y value in a simple linear regression model.

@param x: x position
@param m: slope of the model
@param c: y-intercept of the model
@return: the y value
"""
def predict_y(x, m = 1, c = 0):
    return (x * m + c)

# run if called from command line
def main():
    import argparse
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest = 'func')
    
    # create the parser for the "predict_y" function
    parser_predict_y = subparsers.add_parser('predict_y', help='linear regression y predictor')
    parser_predict_y.add_argument("-x", type = float, required = True, help = 'x value')
    parser_predict_y.add_argument("-m", type = float, default = 1, help = 'slope')
    parser_predict_y.add_argument("-c", type = float, default = 0, help = 'y-intercept')
    
    # parse command line arguments
    args = parser.parse_args()
    if args.func == "predict_y":
        print(predict_y(args.x, m = args.m, c = args.c))

if __name__ == "__main__":
    main()