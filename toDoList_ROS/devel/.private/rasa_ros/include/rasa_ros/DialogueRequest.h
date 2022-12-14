// Generated by gencpp from file rasa_ros/DialogueRequest.msg
// DO NOT EDIT!


#ifndef RASA_ROS_MESSAGE_DIALOGUEREQUEST_H
#define RASA_ROS_MESSAGE_DIALOGUEREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace rasa_ros
{
template <class ContainerAllocator>
struct DialogueRequest_
{
  typedef DialogueRequest_<ContainerAllocator> Type;

  DialogueRequest_()
    : input_text()  {
    }
  DialogueRequest_(const ContainerAllocator& _alloc)
    : input_text(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _input_text_type;
  _input_text_type input_text;





  typedef boost::shared_ptr< ::rasa_ros::DialogueRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rasa_ros::DialogueRequest_<ContainerAllocator> const> ConstPtr;

}; // struct DialogueRequest_

typedef ::rasa_ros::DialogueRequest_<std::allocator<void> > DialogueRequest;

typedef boost::shared_ptr< ::rasa_ros::DialogueRequest > DialogueRequestPtr;
typedef boost::shared_ptr< ::rasa_ros::DialogueRequest const> DialogueRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rasa_ros::DialogueRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rasa_ros::DialogueRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::rasa_ros::DialogueRequest_<ContainerAllocator1> & lhs, const ::rasa_ros::DialogueRequest_<ContainerAllocator2> & rhs)
{
  return lhs.input_text == rhs.input_text;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::rasa_ros::DialogueRequest_<ContainerAllocator1> & lhs, const ::rasa_ros::DialogueRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace rasa_ros

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::rasa_ros::DialogueRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rasa_ros::DialogueRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rasa_ros::DialogueRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rasa_ros::DialogueRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rasa_ros::DialogueRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rasa_ros::DialogueRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rasa_ros::DialogueRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6a278206837cb7b09dde368e542dc10d";
  }

  static const char* value(const ::rasa_ros::DialogueRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6a278206837cb7b0ULL;
  static const uint64_t static_value2 = 0x9dde368e542dc10dULL;
};

template<class ContainerAllocator>
struct DataType< ::rasa_ros::DialogueRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rasa_ros/DialogueRequest";
  }

  static const char* value(const ::rasa_ros::DialogueRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rasa_ros::DialogueRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string input_text\n"
;
  }

  static const char* value(const ::rasa_ros::DialogueRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rasa_ros::DialogueRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.input_text);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct DialogueRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rasa_ros::DialogueRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rasa_ros::DialogueRequest_<ContainerAllocator>& v)
  {
    s << indent << "input_text: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.input_text);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RASA_ROS_MESSAGE_DIALOGUEREQUEST_H
