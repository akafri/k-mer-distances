# kmers-distance
A python program to calculate D1, D2 distances as described [here](http://horn.tau.ac.il/publications/alon_thesis.pdf) for fasta files.

# Prerequisites
This program was tested on Ubuntu 20.0.4 using Python 3. 
Follow these steps before running it:
1. Install Python 3 
   ```
   sudo apt-get install python3
   ```
2. Install Pip
   ```
   sudo apt-get install python3-pip
   ```
3. Install requirements
   ```
   pip3 install -r requirements.txt
   ```
4. Install Jellyfish
   ```
   sudo apt-get install jellyfish
   ```
    or follow the installation instructions here [Jellyfish](https://github.com/gmarcais/Jellyfish) 

# Usage
To run this program, have the fasta files prepared on your filesystem. 
Run the following command:
```
python3 main.py [first_fast_file] [second_fasta_file] [k] [working_directory]
```
Where [first_fast_file] and [second_fasta_file] are the fasta files required for distance calculation, [k] is the kmers size, and [working_directory] is the directory where some temporary files will be written. 

The program will print the following:
```
D1 distance: 0.28380952380952373
.
.
.
D2 distance: 0.1883333333333333
```