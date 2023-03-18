import tensorflow as tf
class NeuralNetHolder:

    def __init__(self):
        super().__init__()

    
    def predict(self, input_row):
        # WRITE CODE TO PROCESS INPUT ROW AND PREDICT X_Velocity and Y_Velocity
        model = tf.keras.models.load_model('true_model.h5')
        prediction = model.predict(input_row)
        result = [prediction[0][0], prediction[0][1]]
        return result
