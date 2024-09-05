import win32print
import os
import sys

def print_html(html_content, printer_name):
    # Create a temporary HTML file
    temp_html_file = 'temp_print.html'
    with open(temp_html_file, 'w') as file:
        file.write(html_content)

    try:
        # Get the default printer if no printer name is provided
        if not printer_name:
            printer_name = win32print.GetDefaultPrinter()

        # Open the printer
        printer_handle = win32print.OpenPrinter(printer_name)

        # Initialize the document properties
        properties = win32print.DEVMODE()
        properties.PaperSize = win32print.DMPAPER_A4
        properties.Orientation = win32print.DMORIENT_PORTRAIT

        # Start the print job
        hprinterjob = win32print.StartDocPrinter(printer_handle, 1, ("Print Job", None, "RAW"))

        # Send the HTML content to the printer
        win32print.StartPagePrinter(printer_handle)
        win32print.WritePrinter(printer_handle, html_content.encode())
        win32print.EndPagePrinter(printer_handle)

        # End the print job
        win32print.EndDocPrinter(printer_handle)

        print(f"Printed successfully to {printer_name}")

    except Exception as e:
        print(f"Error printing: {e}")

    finally:
        # Delete the temporary HTML file
        os.remove(temp_html_file)

if __name__ == "__main__":
    # Get HTML content and printer name from command line arguments
    html_content = sys.argv[1] if len(sys.argv) > 1 else ""
    printer_name = sys.argv[2] if len(sys.argv) > 2 else ""

    # Print HTML on the specified printer
    print_html(html_content, printer_name)
