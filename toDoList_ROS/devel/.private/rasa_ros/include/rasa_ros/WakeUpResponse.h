// Generated by gencpp from file rasa_ros/WakeUpResponse.msg
// DO NOT EDIT!


#ifndef RASA_ROS_MESSAGE_WAKEUPRESPONSE_H
#define RASA_ROS_MESSAGE_WAKEUPRESPONSE_H


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
struct WakeUpResponse_
{
  typedef WakeUpResponse_<ContainerAllocator> Type;

  WakeUpResponse_()
    : ack()  {
    }
  WakeUpResponse_(const ContainerAllocator& _alloc)
    : ack(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _ack_type;
  _ack_type ack;





  typedef boost::shared_ptr< ::rasa_ros::WakeUpResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rasa_ros::WakeUpResponse_<ContainerAllocator> const> ConstPtr;

}; // struct WakeUpResponse_

typedef ::rasa_ros::WakeUpResponse_<std::allocator<void> > WakeUpResponse;

typedef boost::shared_ptr< ::rasa_ros::WakeUpResponse > WakeUpResponsePtr;
typedef boost::shared_ptr< ::rasa_ros::WakeUpResponse const> WakeUpResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rasa_ros::WakeUpResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rasa_ros::WakeUpResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::rasa_ros::WakeUpResponse_<ContainerAllocator1> & lhs, const ::rasa_ros::WakeUpResponse_<ContainerAllocator2> & rhs)
{
  return lhs.ack == rhs.ack;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::rasa_ros::WakeUpResponse_<ContainerAllocator1> & lhs, const ::rasa_ros::WakeUpResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace rasa_ros

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::rasa_ros::WakeUpResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rasa_ros::WakeUpResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rasa_ros::WakeUpResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rasa_ros::WakeUpResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rasa_ros::WakeUpResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rasa_ros::WakeUpResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rasa_ros::WakeUpResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b6a73f722475d64a28238118997ef482";
  }

  static const char* value(const ::rasa_ros::WakeUpResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb6a73f722475d64aULL;
  static const uint64_t static_value2 = 0x28238118997ef482ULL;
};

template<class ContainerAllocator>
struct DataType< ::rasa_ros::WakeUpResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rasa_ros/WakeUpResponse";
  }

  static const char* value(const ::rasa_ros::WakeUpResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rasa_ros::WakeUpResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string ack\n"
;
  }

  static const char* value(const ::rasa_ros::WakeUpResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rasa_ros::WakeUpResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.ack);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct WakeUpResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rasa_ros::WakeUpResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rasa_ros::WakeUpResponse_<ContainerAllocator>& v)
  {
    s << indent << "ack: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.ack);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RASA_ROS_MESSAGE_WAKEUPRESPONSE_H
