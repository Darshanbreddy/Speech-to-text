import azure.cognitiveservices.speech as speechsdk

def recognize_from_mic():
    try:
        # Replace with your actual values
        speech_key = "#Speech API Key"
        speech_region = "#Region"  # e.g., "centralindia"

        # Create Speech configuration
        speech_config = speechsdk.SpeechConfig(
            subscription=speech_key,
            region=speech_region
        )

        # Optional: Set recognition language
        speech_config.speech_recognition_language = "en-US"

        # Use default microphone
        audio_config = speechsdk.AudioConfig(use_default_microphone=True)

        speech_recognizer = speechsdk.SpeechRecognizer(
            speech_config=speech_config,
            audio_config=audio_config
        )

        print("Speak into your microphone...")
        print("Listening...\n")

        result = speech_recognizer.recognize_once_async().get()

        # Handle result
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print(f"RECOGNIZED: {result.text}")

        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized.")

        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation = result.cancellation_details
            print(f"CANCELED: Reason={cancellation.reason}")

            if cancellation.reason == speechsdk.CancellationReason.Error:
                print(f"ErrorCode: {cancellation.error_code}")
                print(f"ErrorDetails: {cancellation.error_details}")
                print("Did you update the speech key and region correctly?")

    except Exception as ex:
        print("An unexpected error occurred:")
        print(str(ex))


if __name__ == "__main__":
    recognize_from_mic()
    input("\nPress Enter to exit...")
