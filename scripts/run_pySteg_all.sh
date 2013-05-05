#!/bin/sh

python scripts/pyStegdetect.py -s 1.0 -p 0.1 -n 50 -t p -c ../data/baseline.csv database/baseline/*.jpg > ../data/baseline_auc.txt
bark

python scripts/pyStegdetect.py -s 1.0 -p 0.1 -n 50 -t p -c ../data/blur.csv database/blur/*.jpg > ../data/blur_auc.txt
bark

python scripts/pyStegdetect.py -s 1.0 -p 0.1 -n 50 -t p -c ../data/contrast.csv database/contrast/*.jpg > ../data/contrast_auc.txt
bark

python scripts/pyStegdetect.py -s 1.0 -p 0.1 -n 50 -t p -c ../data/emboss.csv database/emboss/*.jpg > ../data/emboss_auc.txt
bark

python scripts/pyStegdetect.py -s 1.0 -p 0.1 -n 50 -t p -c ../data/gotham.csv database/gotham/*.jpg > ../data/gotham_auc.txt
bark

python scripts/pyStegdetect.py -s 1.0 -p 0.1 -n 50 -t p -c ../data/kelvin.csv database/kelvin/*.jpg > ../data/kelvin_auc.txt
bark

python scripts/pyStegdetect.py -s 1.0 -p 0.1 -n 50 -t p -c ../data/lomo.csv database/lomo/*.jpg > ../data/lomo_auc.txt
bark

python scripts/pyStegdetect.py -s 1.0 -p 0.1 -n 50 -t p -c ../data/nashville.csv database/nashville/*.jpg > ../data/nashville_auc.txt
bark

python scripts/pyStegdetect.py -s 1.0 -p 0.1 -n 50 -t p -c ../data/noise.csv database/noise/*.jpg > ../data/noise_auc.txt
bark

python scripts/pyStegdetect.py -s 1.0 -p 0.1 -n 50 -t p -c ../data/saturate.csv database/saturate/*.jpg > ../data/saturate_auc.txt
bark

python scripts/pyStegdetect.py -s 1.0 -p 0.1 -n 50 -t p -c ../data/sigmoidal.csv database/sigmoidal/*.jpg > ../data/sigmoidal_auc.txt
bark

python scripts/pyStegdetect.py -s 1.0 -p 0.1 -n 50 -t p -c ../data/tiltshift.csv database/tiltshift/*.jpg > ../data/tiltshift_auc.txt
bark

python scripts/pyStegdetect.py -s 1.0 -p 0.1 -n 50 -t p -c ../data/toaster.csv database/toaster/*.jpg > ../data/toaster_auc.txt
bark

