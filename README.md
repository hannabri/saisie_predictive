# Saisie prédictive - Projet TAL L3

## La saisie prédictive, qu'est-ce que c'est&nbsp;?

Vous avez sûrement déjà utilisé des outils qui utilisent de la saise prédictive&nbsp;! Elle aide l'utilisateur à écrire des messages et propose généralement une liste de mots. Le but de la saisie prédictive est d'essayer de prédire et de compléter le message à l'aide de cette liste de mots proposée. Elle est généralement utilisée dans le contexte des messages SMS ou des messages instantantés mais nous la trouvons également dans les logiciel d'envoie de courriel. 

La saisie prédictive est composée de deux parties : la prédiction et la complétion. Parfois, ces parties sont des étapes consécutives quand par exemple la liste proposée ne contient pas le mot souhaité. Dans d'autres cas ces deux parties sont utilisées individuellement. Si le mot souhaité apparait dans la liste avec les prédiction, l'utilisateur a déjà trouvé le mot et n'utilise plus la complétion. En début de phrase, notre programme ne peut pas encore proposé des mots donc seule la complétion pourra aider l'utilisateur à écrire le mot. 

### Prédiction 

Comme le nom l'indique, lors de la prédiction le programme essaie de prédire le prochain mot que l'utilisateur va utiliser, sans que celui-ci n'en ait saisie la première lettre. Pour cela, il se base sur de calculs probabilistes afin de trouver les mots les plus probables dans le contexte. Le contexte dans notre programme se compose seulement du dernier mot saisi mais il d'autres modèles prennent également l'avant-dernier mot saisi en compte. La prédiction est donc le fait de prédire le mot qui suit le dernier mot (ou les deux derniers mots) saisi. 

### Complétion

Le nom de la complétion est également très parlant. Pour cette partie, le programme essaie de compléter le mot que l'utilisateur est en train de saisir. La différence avec la prédiction ? Pour la complétion, l'utilisateur a déjà commencé à saisir le mot. Il a au moins déjà tappé la première lettre. Ce début de mot est appelé <i>préfixe</i>. Ce préfixe est important pour le programme afin qu'il puisse chercher tous les mots commençant avec cette suite de lettres et en proposer les plus probables. La complétion essaie alors de compléter un mot dont l'utilisateur a saisi au moins une lettre.   

## Pourquoi la saisie prédictive&nbsp;?

La saisie prédictive est surtout un outil qui facilite la rédaction des messages pour l'utilisateur. À l'aide de cet outil, il doit dans le meilleur des cas seulement saisir quelques lettres pour écrire un message complet. Ainsi, la rédaction va plus vite et dans l'idéal le message contient moins de fautes d'orthographes.  

## Et en cas de problème&nbsp;?

Si vous rencontrer des problémes avec notre programme, nous avons fait une aide en ligne à laquell vous pouvez accéder avec <a href="http://htmlpreview.github.io/?https://raw.githubusercontent.com/rfclara/prediction/main/aide.html?token=GHSAT0AAAAAACDPKZII6H6GLHZL2SXC5RMSZEF7DAQ">ce lien</a>.

## Qui sommes-nous&nbsp;?

Nous sommes trois étudiantes en Science de Langage parcours Linguistique et Informatique à l'Université Paris Cité. Ce programme dans le domaine du traitement automatique des langues constitue notre projet de fin d'année en licence 3.
