Nombre: Pedro Mérida Álvarez   Rol: 201773583-K

Descripcion:
Tarea 1 del ramo Prueba de Software (Validación y Verificación)

Instalacion:
Se necesita python 3.x para la ejecucion de esta tarea.

Como usar:
Para ejecutar, debe posicionarse en la carpeta donde esta el archivo "tarea1.py" y abrir una terminal en dicha carpeta, luego escribir el siguiente comando:

Si se esta en Windows: python tarea1.py
Si se esta en Linux: python3 tarea1.py

Luego seguir las instrucciones que aparecen en pantalla

Como contribuir:
Fork the repository
At the top right corner, you will see the term "fork". All you need to do is click it and you will have created a copy of the same project in your account.

Clone the project into your local machine
Copy the forked project URL, and proceed to your local machine where you will open git bash, and proceed with the command below:

git clone https://github.com/<YourUserName>/<projectname>

This will create a copy of the project on your local machine. Now that you have cloned the repo we will need to do two things:

First is to make the necessary changes/contribution and commit those changes. After making your changes and adding new files, its time to add those changes into a separate branch before pushing them to remote.

But, first let's create a branch. In your git bash, change the path to pint to your repository directory. To do that use this command:

cd project folder name

Now, to create a branch we will use the command: git checkout

git checkout -b your-new-branch-name

It's time to add the new changes into the branch we created. In order to see all the changes you made, we will use the git status command:

git status

The command will list all the changes you made. To add them we will use git add *, which will add all the files to our branch.

git add *

Let's add a commit message, briefly explaining what we added:

git commit -m "<message here>"

Push changes to remote
Now that everything is set, it's time to let our maintainer know what we have added. That is made possible by pushing the changes with this command:

git push origin <add-your-branch-name>

Submit changes
If you go to your repository on GitHub and refresh the page, you'll see a Compare and pull request button. Click on that button.

Soon the maintainer will merge all your changes into the master branch of this project (unless they need changes from you). You will get a notification email once the changes have been merged.

Licencia:
Copyright (c) 2022 Pedro Dante Mérida Álvarez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.