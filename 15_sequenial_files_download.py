import os
import re
import urllib.parse
import urllib.request

def download_files(first_url, output_dir):
    # Ensure output directory exists; create if not.
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract filename and directory from the first URL.
    url_head, url_tail = os.path.split(first_url)
    
    # Extract the last sequence of digits from the filename.
    first_index = re.findall(r'\d+', url_tail)[-1]
    
    index_count, error_count = 0, 0
    max_errors = 5
    
    while error_count < max_errors:
        next_index = str(int(first_index) + index_count)
        
        # Maintain zero-padding if the first index was zero-padded.
        if first_index[0] == '0':
            next_index = next_index.zfill(len(first_index))
        
        # Construct the next URL with the updated index.
        next_url = urllib.parse.urljoin(url_head, re.sub(r'\d+', next_index, url_tail))
        
        try:
            # Prepare the output file path.
            output_file = os.path.join(output_dir, os.path.basename(next_url))
            
            # Download the file from the constructed URL.
            urllib.request.urlretrieve(next_url, output_file)
            
            # Print success message upon successful download.
            print(f'Successfully downloaded {os.path.basename(next_url)}')
        
        except IOError:
            # Handle errors when URL retrieval fails.
            print(f'Could not retrieve {next_url}')
            error_count += 1
        
        # Increment index count for the next iteration.
        index_count += 1

if __name__ == '__main__':
    # Example usage:
    download_files('http://699340.youcanlearnit.net/image001.jpg', 'images')
