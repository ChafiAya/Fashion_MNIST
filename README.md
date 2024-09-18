# Fashion-MNIST CNN Classification 
Exercice 1 : Apprentissage automatique supervisé (Classification)
Objectif

Créer un modèle d'IA capable de reconnaître et de classifier des images à l'aide d'un réseau de neurones convolutif (CNN) avec la bibliothèque Keras.
Étape 1 : Préparation de l'environnement

    Installation des bibliothèques nécessaires : J'ai installé les bibliothèques suivantes en utilisant pip :

    pip install tensorflow keras matplotlib seaborn scikit-learn

Étape 2 : Chargement du dataset et normalisation

    Chargement du dataset Fashion-MNIST : J'ai chargé le dataset en utilisant la fonction tf.keras.datasets.fashion_mnist.load_data(), ce qui m'a permis d'obtenir les ensembles d'entraînement et de test.

    Normalisation des images : J'ai normalisé les images en les convertissant en type float32 et en les divisant par 255.0. Cela a permis de ramener les valeurs des pixels entre 0 et 1.

    Affichage d'une image du dataset : J'ai affiché une image du dataset avec son étiquette associée en utilisant matplotlib. L'étiquette est identifiée par son index dans le tableau des étiquettes.

Étape 3 : Création du modèle CNN

    Reshape des images : J'ai modifié la forme des images pour les adapter à l'entrée du modèle CNN, en les transformant en (28, 28, 1).

    Création du modèle CNN : J'ai construit un modèle avec plusieurs couches de convolution (Conv2D) et de pooling (MaxPooling2D), suivi de couches denses pour la classification.

    Compilation du modèle : Lors de la compilation du modèle, j'ai utilisé les paramètres suivants :
        Optimiseur : Adam
        Fonction de perte : SparseCategoricalCrossentropy
        Métriques : Précision (accuracy)

Étape 4 : Entraînement du modèle

    Entraînement du modèle : J'ai entraîné le modèle en utilisant l'ensemble d'entraînement, en définissant des paramètres comme le nombre d'époques (EPOCHS) et la taille de batch (BATCH_SIZE). J'ai également utilisé des callbacks pour la réduction du taux d'apprentissage et l'arrêt précoce.

    Évaluation du modèle : Après l'entraînement, j'ai évalué la précision du modèle sur l'ensemble de test, obtenant ainsi un aperçu de ses performances.

Étape 5 : Visualisation des prédictions

    Prédiction sur les données de test : J'ai utilisé le modèle pour prédire les classes des images de test, en appliquant une couche Softmax pour obtenir des probabilités.

    Affichage des résultats : J'ai créé une fonction pour afficher une image, la prédiction du modèle, et l'étiquette réelle. J'ai observé les résultats pour évaluer la performance du modèle, en utilisant des couleurs pour indiquer la justesse des prédictions (vert pour correct, rouge pour incorrect).