<?php 
require 'functions.php';
$pdo = connexion();
require 'header.php';
$erreur = null;
$succes = null;
if(isset($_POST['submit']))
{
    if(!empty($_POST['pseudonyme']) && !empty($_POST['email']) && !empty($_POST['mdp']) && !empty($_POST['mdpc']) && !empty($_FILES['monfichier']))
    {
        $pseudonyme = htmlspecialchars($_POST['pseudonyme']);
        $email = htmlspecialchars($_POST['email']);
        $mdp = htmlspecialchars($_POST['mdp']);
        $mdpc = htmlspecialchars($_POST['mdpc']);

        if(!filter_var($email, FILTER_VALIDATE_EMAIL))
        {
            $erreur[] = "Merci de renseigner un e-mail valide.";
        }   
        if($mdp !== $mdpc)
        {
            $erreur[] = "Les deux mots de passe sont différents.";
        }
        if(strlen($pseudonyme) < 2)
        {
            $erreur[] = "Le pseudonyme est trop court";
        }

        //On vérifie si l'upload s'est bien déroulé
        if(isset($_FILES['monfichier']) && $_FILES['monfichier']['error'] == 0)
        {
            //On vérifie si le fichier n'est pas trop gros
            if($_FILES['monfichier']['size'] <= 250000)
            {
                //On vérifie si l'utilisateur a bien uploadé un fichier avec une extension autorisée
                $infofichier = pathinfo($_FILES['monfichier']['name']);

                //On récupère l'extension (.png, .jpg etc.) et le filename (nom du fichier sans extension (soleil))
                $extension = $infofichier['extension'];
                $filename = $infofichier['filename'];

                $extensions_autorisees = array('jpg', 'jpeg', 'gif', 'png');

                //In array permet de voir si une valeur est présente dans un tableau
                //Dans notre cas on regarde si $extension est présent dans le tableau d'extensions autorisees
                if(in_array($extension, $extensions_autorisees))
                {
                    //On va réecrire le nom du fichier.
                    //On a le nom du fichier de l'utilisateur grâce à $_FILES['monfichier']['name'];
                    //Ci-dessus on avait, grâce à la fonction pathinfo récupéré l'extension du fichier ainsi que son nom sans extension
                    $nomdufichierauploader = $filename.time().'.'.$extension;


                    //On place le fichier qui est pour le moment stocké temporairement sur le serveur à l'endroit de notre choix.
                    $resultat = move_uploaded_file($_FILES['monfichier']['tmp_name'], 'uploads/img/'.$nomdufichierauploader);
                    if(!$resultat)
                    {
                        $erreur[] = 'Une erreur est survenue lors de l\'upload.';
                    }
                }
                else 
                {
                    $erreur[] = 'L\'extension du fichier n\'est pas autorisée.';
                }
            }  
            else 
            {
                $erreur[] = 'Le fichier uploadé est trop gros';
            }  
        }
        else 
        {
            $erreur[] = 'Une erreur est survenue lors de l\'upload';
        }


        if(!$erreur)
        {
            $sql = 'INSERT INTO users (pseudonyme,motdepasse,email,avatar,is_admin)
            VALUES(:pseudonyme, :motdepasse, :email, :avatar, :is_admin)';
            $requete = $pdo->prepare($sql);
            $resultat = $requete->execute(array(
                'pseudonyme' => $pseudonyme,
                'motdepasse' => password_hash($mdp, PASSWORD_BCRYPT),
                'email' => $email,
                'avatar' => $nomdufichierauploader,
                'is_admin' => 0
            ));
            if(!$resultat)
            {
                $erreur[] = "Une erreur s'est produite pendant l'insertion dans la bdd";
            }
            else 
            {
                $succes = "Vous avez bien été inscrit.";
            }
        }

    }
    else 
    {
        $erreur[] = "Merci de remplir tous les champs.";
    }
}
?>

<div class="container">
    <div class="row">
        <div class="col-md-12">
            <h1>Inscription</h1>
            <?php 
            if($erreur)
            {
                foreach($erreur as $err)
                {
                    echo $err.'<br />';
                }
            }
            if($succes)
            {
                echo $succes.'<br />';
            }
            else 
            {
            ?>
            <form action="" method="POST" enctype="multipart/form-data">
                <div class="form-group">
                    <label for="pseudonyme">Pseudonyme</label>
                    <input type="text" class="form-control" id="pseudonyme" name="pseudonyme" />
                </div>
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" class="form-control" id="email" name="email" />
                </div>
                <div class="form-group">
                    <label for="mdp">Mot de passe</label>
                    <input type="password" class="form-control" id="mdp" name="mdp" />
                </div>
                <div class="form-group">
                    <label for="mdpc">Confirmation mot de passe</label>
                    <input type="password" class="form-control" id="mdpc" name="mdpc" />
                </div>
                <div class="form-group">
                    <label for="fichier">Avatar</label>
                    <input type="file" id="fichier" name="monfichier" />
                </div>
                <div class="form-group">
                    <button type="submit" name="submit" class="btn btn-primary">Inscription</button>
                </div>
            </form>
            <?php 
            }
            ?>
        </div>
    </div>
</div>

<?php require 'footer.php'; ?>