#!/bin/csh

set FNAME=`ls *swfl.filt.tif | head -1`
echo $FNAME

if ("$FNAME" == "") then 
	exit
endif  

ibmcloud cos put-object --bucket noaaprelabeled --key $FNAME --body $FNAME

rm $FNAME 

echo "$FNAME removed"

./copyToCOS.csh

