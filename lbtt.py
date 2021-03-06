class TaxBand:
      def __init__(self, low, high, rate):
          self.low = low
          self.high = high
          self.rate = rate
          
def calculate_lbtt(property_value):
    
    tax_bands = [TaxBand(0,145000,0),TaxBand(145000,250000,0.02),TaxBand(250000,325000,0.05),TaxBand(325000,750000,0.1),TaxBand(750000,float('inf'),0.12)]
    bands = []
    tax = 0
    
    for band in tax_bands:
        if band.low < property_value:
            bands.append(band)
    
    for band in bands:
        if band.high < property_value:
            tax += (band.high-band.low)*band.rate
        else:
            tax += (property_value-band.low)*band.rate
    
    return round(tax,2)

if __name__ == "__main__":
    property_value = float(input("Enter: "))
    # poperty_value = 325000
    tax = calculate_lbtt(property_value)
    print(tax)