from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(max(result , key=result.get), 'joy')

        result = emotion_detector("I am really mad about this")
        self.assertEqual(max(result , key=result.get), 'anger')

        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(max(result , key=result.get), 'disgust')

        result = emotion_detector("I am so sad about this")
        self.assertEqual(max(result , key=result.get), 'sadness')

        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(max(result , key=result.get), 'fear')

if __name__ == '__main__':
    unittest.main()

