# A script to create shared dataset directory at the top most level
mkdir /shared_datasets
chmod u+x,g=rx,o=rx /shared_datasets
echo "The admin can place shared dataset in this directory so that every user does not have to re-download it" | cat > /shared_datasets/readme.txt
