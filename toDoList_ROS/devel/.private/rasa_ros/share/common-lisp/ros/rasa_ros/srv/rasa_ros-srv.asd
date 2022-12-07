
(cl:in-package :asdf)

(defsystem "rasa_ros-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Dialogue" :depends-on ("_package_Dialogue"))
    (:file "_package_Dialogue" :depends-on ("_package"))
    (:file "Rest" :depends-on ("_package_Rest"))
    (:file "_package_Rest" :depends-on ("_package"))
    (:file "Text2Speech" :depends-on ("_package_Text2Speech"))
    (:file "_package_Text2Speech" :depends-on ("_package"))
    (:file "WakeUp" :depends-on ("_package_WakeUp"))
    (:file "_package_WakeUp" :depends-on ("_package"))
  ))