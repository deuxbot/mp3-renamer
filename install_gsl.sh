#!/bin/bash
if [ "$#" -ne 1 ]; then
	echo "Usage ./install_gsl.sh installPath"
	exit
fi
DEST_PATH=$1
wget ftp://ftp.gnu.org/gnu/gsl/gsl-2.1.tar.gz 
tar -xzvf gsl-2.1.tar.gz 
rm gsl-2.1.tar.gz
cd gsl-2.1
./configure --prefix=$DEST_PATH
make
make check
make install
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DEST_PATH/lib' >> ~/.bashrc 
echo 'export LIBRARY_PATH=$LIBRARY_PATH:$DEST_PATH/lib' >> ~/.bashrc 
rm -rf ../gsl-2.1
