def get_http_error(error_code):
    result = ""

    match error_code:
        case 200:
            result = "OK"
        case 400:
            result = "Bad Request"
        case 404:
            result = "Not found"
        case _:
            result = "Unknown error"
    
    return result

def main():
    print(get_http_error(error_code= 404))

if __name__ == "__main__":
    main()