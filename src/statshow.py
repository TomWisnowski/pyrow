import pyrow
import time
#import json
import pickle

if __name__ == '__main__':
    # Connecting to erg
    machines_list = list(pyrow.find())

    # with open('listfile.data', 'rb') as filehandle:
    # read the data as binary data stream
    ## ergs = pickle.load(filehandle)

    if len(machines_list) == 0:
        exit("No ergs found.")

   # with open('listfile.data', 'wb') as filehandle:
    # store the data as binary data stream
   ##  pickle.dump(ergs, filehandle)

    # with open('ErgResults.txt', 'w') as filehandle:
    # json.dump(ergs, filehandle)
    # with open('ErgResults.txt', 'w') as f:
    # f.write(json.dumps(ergs))

    # Now read the file back into a Python list object
    # with open('ErgResults.txt', 'r') as f:
    # ergs = json.loads(f.read())

    work_out_machine = pyrow.pyrow(machines_list[0])
    print ("Connected to erg.")

    # Create a dictionary of the different status states
    state = ['Error', 'Ready', 'Idle', 'Have ID', 'N/A', 'In Use',
             'Pause', 'Finished', 'Manual', 'Offline']

    stroke = ['Wait for min speed', 'Wait for acceleration',
              'Drive', 'Dwelling', 'Recovery']

    workout = ['Waiting begin',
               'Workout row',
               'Countdown pause',
               'Interval rest',
               'Work time inverval',
               'Work distance interval',
               'Rest end time',
               'Rest end distance',
               'Time end rest',
               'Distance end rest',
               'Workout end',
               'Workout terminate',
               'Workout logged',
               'Workout rearm']

    command1 = [
        'CSAFE_PM_GET_WORKOUTSTATE',
        'CSAFE_PM_GET_STROKESTATE',
        'CSAFE_GETSTATUS_CMD',
        'CSAFE_RESET_CMD',
        'CSAFE_GOIDLE_CMD',
        'CSAFE_GOHAVEID_CMD',
        'CSAFE_GOINUSE_CMD',
        'CSAFE_GOFINISHED_CMD',
        'CSAFE_GOREADY_CMD',
        'CSAFE_BADID_CMD',
        'CSAFE_GETVERSION_CMD',
        'CSAFE_GETID_CMD',
        'CSAFE_GETUNITS_CMD',
        'CSAFE_GETSERIAL_CMD']
    
    command2 =[
        'CSAFE_GETODOMETER_CMD',
        'CSAFE_GETERRORCODE_CMD',
        'CSAFE_GETTWORK_CMD',
        'CSAFE_GETHORIZONTAL_CMD',
        'CSAFE_GETCALORIES_CMD',
        'CSAFE_GETPROGRAM_CMD',
        'CSAFE_GETPACE_CMD',
        'CSAFE_GETCADENCE_CMD',
        'CSAFE_GETUSERINFO_CMD',
        'CSAFE_GETHRCUR_CMD',
        'CSAFE_GETPOWER_CMD',
    ]
    # command = [
# cmds['CSAFE_GETSTATUS_CMD'] = [0x80, []]
# cmds['CSAFE_RESET_CMD'] = [0x81, []]
# cmds['CSAFE_GOIDLE_CMD'] = [0x82, []]
# cmds['CSAFE_GOHAVEID_CMD'] = [0x83, []]
# cmds['CSAFE_GOINUSE_CMD'] = [0x85, []]
# cmds['CSAFE_GOFINISHED_CMD'] = [0x86, []]
# cmds['CSAFE_GOREADY_CMD'] = [0x87, []]
# cmds['CSAFE_BADID_CMD'] = [0x88, []]
# cmds['CSAFE_GETVERSION_CMD'] = [0x91, []]
# cmds['CSAFE_GETID_CMD'] = [0x92, []]
# cmds['CSAFE_GETUNITS_CMD'] = [0x93, []]
# cmds['CSAFE_GETSERIAL_CMD'] = [0x94, []]
# cmds['CSAFE_GETODOMETER_CMD'] = [0x9B, []]
# cmds['CSAFE_GETERRORCODE_CMD'] = [0x9C, []]
# cmds['CSAFE_GETTWORK_CMD'] = [0xA0, []]
# cmds['CSAFE_GETHORIZONTAL_CMD'] = [0xA1, []]
# cmds['CSAFE_GETCALORIES_CMD'] = [0xA3, []]
# cmds['CSAFE_GETPROGRAM_CMD'] = [0xA4, []]
# cmds['CSAFE_GETPACE_CMD'] = [0xA6, []]
# cmds['CSAFE_GETCADENCE_CMD'] = [0xA7, []]
# cmds['CSAFE_GETUSERINFO_CMD'] = [0xAB, []]
# cmds['CSAFE_GETHRCUR_CMD'] = [0xB0, []]
# cmds['CSAFE_GETPOWER_CMD'] = [0xB4, []]]

    # prime status number
    cstate = -1
    cstroke = -1
    cworkout = -1

    work_out_machine.set_workout(distance=2000, split=100, pace=120)

    # Inf loop
    while 1:
        results1 = work_out_machine.send(command1)
        results2 = work_out_machine.send(command2)
        print ("results1 " + str(results1))
        print ("results2 " + str(results2))
        if cstate != (results1['CSAFE_GETSTATUS_CMD'][0] & 0xF):
            cstate = results1['CSAFE_GETSTATUS_CMD'][0] & 0xF
            print ("State " + str(cstate) + ": " + state[cstate])
        if cstroke != results1['CSAFE_PM_GET_STROKESTATE'][0]:
            cstroke = results1['CSAFE_PM_GET_STROKESTATE'][0]
            print ("Stroke " + str(cstroke) + ": " + stroke[cstroke])
        if cworkout != results1['CSAFE_PM_GET_WORKOUTSTATE'][0]:
            cworkout = results1['CSAFE_PM_GET_WORKOUTSTATE'][0]
            print ("Workout " + str(cworkout) + ": " + workout[cworkout])
        time.sleep(1)

        # Looks like results {'CSAFE_GETCADENCE_CMD': [25, 84], 'CSAFE_GETPACE_CMD': [555, 57], 'CSAFE_PM_GET_STROKESTATE': [1], 'CSAFE_GETUNITS_CMD': [0],
# 'CSAFE_GETTWORK_CMD': [0, 2, 29], 'CSAFE_PM_GET_WORKOUTSTATE': [1], 'CSAFE_GETSTATUS_CMD': [137], 'CSAFE_GETPOWER_CMD': [16, 88]}

# Looks like 'CSAFE_GETPOWER_CMD': [16, 88]'   The 16 correlates to the amount of effort the user puts in.
# going slow with the resistence all the way up is basically the same as going fast but the resistance all the way low.add()


#   CSAFE_GETCADENCE_CMD': [25, 84]   25 = the number of strokes per minute

#
