#!/bin/bash

REGIONS=$(aws ec2 describe-regions --query "Regions[].RegionName" --output text)

for region in $REGIONS; do
  echo "Unattached gp2 volumes in $region:"
  aws ec2 describe-volumes --region "$region" --filters Name=status,Values=available Name=volume-type,Values=gp2 | jq -r '.Volumes[] | .VolumeId'
done

