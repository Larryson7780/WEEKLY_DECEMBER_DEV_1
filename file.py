import streamlit as st
import enchant


def corriger_texte(texte, langue):
    if langue == 'fr':
        d = enchant.Dict('fr_FR')
    elif langue == 'en':
        d = enchant.Dict('en_US')
    else:
        raise ValueError('Langue non prise en charge')

    phrases = texte.split('\n')
    phrases_corrigees = []

    for phrase in phrases:
        mots = phrase.split()
        mots_corriges = [d.suggest(mot)[0] if not d.check(mot) else mot for mot in mots]
        phrase_corrigee = ' '.join(mots_corriges)
        phrases_corrigees.append(phrase_corrigee)

    texte_corrigé = '\n'.join(phrases_corrigees)
    return texte_corrigé


def main():
    st.title('Correction de texte')

    texte_original = st.text_area('Entrez votre texte (une phrase par ligne):')

    # Choix de la langue
    langue = st.radio('Choisir la langue de correction:', ['fr', 'en'])

    if st.button('Soumettre'):
        texte_corrigé = corriger_texte(texte_original, langue)
        st.subheader('Texte corrigé:')
        st.write(texte_corrigé)


if __name__ == '__main__':
    main()
