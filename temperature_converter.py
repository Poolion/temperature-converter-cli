def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Convert temperatures between Celsius and Fahrenheit.')
    parser.add_argument('value', type=float, help='Temperature value to convert')
    parser.add_argument('scale', choices=['celsius', 'fahrenheit'], help='Scale of the input temperature')
    parser.add_argument('target_scale', choices=['celsius', 'fahrenheit'], help='Target scale for conversion')
    args = parser.parse_args()

    if args.scale == 'celsius':
        result = celsius_to_fahrenheit(args.value)
        print(f'{args.value}°C is equivalent to {result:.2f}°F')
    elif args.scale == 'fahrenheit':
        result = fahrenheit_to_celsius(args.value)
        print(f'{args.value}°F is equivalent to {result:.2f}°C')

if __name__ == '__main__':
    main()