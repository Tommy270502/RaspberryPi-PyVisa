import pyvisa
#Create a resource manager
resources = pyvisa.ResourceManager('@py')
#Open the DSO by name. (Change this to the string for your instrument)
oscilloscope = resources.open_resource('YOURINSTRUMENTSTRING')
#Return the DSO's ID string to tell us it's there
print(oscilloscope.query('*IDN?'))
#Close the connection
oscilloscope.close()
