import streamlit as st
import cv2
import numpy as np

def main():
    st.title("Application de Webcam avec Streamlit")

    # Démarrer la webcam
    cap = cv2.VideoCapture(0)

    stframe = st.empty()

    while True:
        ret, frame = cap.read()
        print(ret)
        print(frame)
        if not ret:
            st.write("Impossible d'accéder à la webcam.")
            break

        # Convertir l'image de BGR à RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Afficher l'image sur la page web
        stframe.image(frame, channels='RGB')

        # Arrêter la webcam si le bouton est cliqué
        # if st.button('Arrêter la webcam'):
        #     break

    cap.release()

if __name__ == "__main__":
    main()
