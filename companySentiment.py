#import to use as modules, perhaps for unit testing
import twitterAPI
import googleAPI


def main():
  #run the two files sequentially to generate results
  execfile('TwitterAPI.py')
  execfile('googleAPI.py')

if __name__ == "__main__":
    main()
