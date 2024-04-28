import qrcode
import curses
import datetime

def convert_to_binary(data):
    # Convert data to binary
    binary_data = ' '.join(format(ord(char), '08b') for char in data)
    return binary_data

def generate_qr_code(data, file_name):
    # Convert data to binary
    binary_data = convert_to_binary(data)
    
    # Generate QR code from binary data
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=2,
    )
    qr.add_data(binary_data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code image
    qr_image.save(file_name)
    return file_name

def draw_menu(stdscr):
    # Turn off cursor blinking
    curses.curs_set(1)

    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

    while True:
        # Clear screen
        stdscr.clear()

        # Print header
        header = "QR Code Generator"
        stdscr.addstr(2, curses.COLS // 2 - len(header) // 2, header, curses.color_pair(1))
        stdscr.addstr(3, curses.COLS // 2 - len(header) // 2, '-' * len(header), curses.color_pair(2))

        # Get user input for name
        stdscr.addstr(5, 2, "Enter Name: ")
        stdscr.refresh()
        name = ""
        while True:
            key = stdscr.getch()
            if key == curses.KEY_ENTER or key == 10:
                break
            elif key == curses.KEY_BACKSPACE:
                name = name[:-1]
            elif key == ord('q'):
                return
            else:
                name += chr(key)
            stdscr.clear()
            stdscr.addstr(5, 2, "Enter Name: " + name)
            stdscr.refresh()

        # Get user input for certificate ID
        stdscr.addstr(7, 2, "Enter Certificate ID: ")
        stdscr.refresh()
        certificate_id = ""
        while True:
            key = stdscr.getch()
            if key == curses.KEY_ENTER or key == 10:
                break
            elif key == curses.KEY_BACKSPACE:
                certificate_id = certificate_id[:-1]
            elif key == ord('q'):
                return
            else:
                certificate_id += chr(key)
            stdscr.clear()
            stdscr.addstr(7, 2, "Enter Certificate ID: " + certificate_id)
            stdscr.refresh()

        # Get user input for date
        stdscr.addstr(9, 2, "Enter Date (YYYY-MM-DD): ")
        stdscr.refresh()
        date_str = ""
        while True:
            key = stdscr.getch()
            if key == curses.KEY_ENTER or key == 10:
                try:
                    datetime.datetime.strptime(date_str, '%Y-%m-%d')
                    break
                except ValueError:
                    stdscr.addstr(10, 2, "Invalid date format. Please enter in YYYY-MM-DD format.")
                    stdscr.refresh()
                    date_str = ""
                    continue
            elif key == curses.KEY_BACKSPACE:
                date_str = date_str[:-1]
            elif key == ord('q'):
                return
            else:
                date_str += chr(key)
            stdscr.clear()
            stdscr.addstr(9, 2, "Enter Date (YYYY-MM-DD): " + date_str)
            stdscr.refresh()

        # Get user input for certificate for
        stdscr.addstr(11, 2, "Enter Certificate For: ")
        stdscr.refresh()
        certificate_for = ""
        while True:
            key = stdscr.getch()
            if key == curses.KEY_ENTER or key == 10:
                break
            elif key == curses.KEY_BACKSPACE:
                certificate_for = certificate_for[:-1]
            elif key == ord('q'):
                return
            else:
                certificate_for += chr(key)
            stdscr.clear()
            stdscr.addstr(11, 2, "Enter Certificate For: " + certificate_for)
            stdscr.refresh()

        certificate_info = f"Name: {name}, Certificate ID: {certificate_id}, Date: {date_str}, Certificate For: {certificate_for}"

        # Generate QR code
        file_name = f"{name}_certificate_qr_code.png"
        generate_qr_code(certificate_info, file_name)

        stdscr.addstr(curses.LINES - 2, 0, f"QR code saved as {file_name}. Press 'q' to quit or any other key to continue...")
        stdscr.refresh()

        # Wait for user input
        key = stdscr.getch()
        if key == ord('q'):
            return

curses.wrapper(draw_menu)
