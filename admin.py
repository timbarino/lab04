class Admin():
      def __init__(self,name,ID,user_name,pass_word):
         self._name = name
         self._ID = ID
         self._user_name = user_name
         self._pass_word = pass_word

      def change_name(self,name):
         self._name = name
      def change_name(self,ID):
         self._ID = ID
      def change_name(self,user_name):
         self._user_name = user_name
      def change_name(self,pass_word):
         self._pass_word = pass_word
      def get_user_name(self):
         return self._user_name
      def get_pass_word(self):
         return self._pass_word
