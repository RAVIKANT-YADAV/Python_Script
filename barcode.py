
import barcode
import EAN-13

# Make sure to pass the number as string
number = '5901234123457'

# Now, let's create an object of EAN13
# class and pass the number
my_code = EAN13(number)
# Our barcode is ready. Let's save it.
my_code.save("new_code")

python-barcode create -t png "My Text" outfile
python-barcode create "123456789000" outfile -b ean --text "text to appear under barcode