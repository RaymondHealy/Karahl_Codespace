double fMap(double src, double fromLow, double fromHigh, double toLow, double toHigh) {
  //Find the place of <src> in the range (remove the floor and divide the
  //    remainder by the size of the range) and saves it to <src>
  src = (src - fromLow) / (fromHigh - fromLow);

  //Multiply that <src> value over the output range to find the delta from
  //    the min value, add that delta to the low point in the cast range
  return toLow + src * (toHigh - toLow);
}