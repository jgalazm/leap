import sys
sys.path.insert(0, "../lib")
import Leap



class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']

    def on_init(self, controller):
        print("Initialized") 

    def on_connect(self, controller):
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
        print("Connected") 

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print("Disconnected") 

    def on_exit(self, controller):
        print("Exited") 

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        print "Frame ID:"+ str(frame.id) \
		+ "Timestamp: " + str(frame.timestamp) \
		+ "# of Hands: " + str(len(frame.hands)) \
		+ "# of Fingers: " + str(len(frame.fingers)) \
		+ "# of Tools: " + str(len(frame.tools)) \
		+ "# of Gestures: " + str(len(frame.gestures()))
        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = Leap.SwipeGesture(gesture)
                start = swipe.start_position
                current = swipe.position
                direction = swipe.direction
                velocity = swipe.speed
                swipper = swipe.pointable
                print "swipe: "
                print "\t start:", start
                print "\t current:", current
                print "\t current:", current
                print "\t direction:", direction
                print "\t velocity:", velocity


        
def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()
    


    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
