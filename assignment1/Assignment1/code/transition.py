class Transition(object):
    """
    This class defines a set of transitions which are applied to a
    configuration to get the next configuration.
    """
    # Define set of transitions
    LEFT_ARC = 'LEFTARC'
    RIGHT_ARC = 'RIGHTARC'
    SHIFT = 'SHIFT'
    REDUCE = 'REDUCE'

    def __init__(self):
        raise ValueError('Do not construct this object!')

    @staticmethod
    def left_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        #print 'leftarc'
        if not conf.buffer or not conf.stack:
            return -1
        s = conf.stack[-1]
        if s==0:
            return -1
        
        if any(s == wi for wk, l, wi in conf.arcs):
            return -1
        b = conf.buffer[0]
        conf.stack.pop()
        conf.arcs.append((b,relation,s))
    @staticmethod
    def right_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        #print 'rightarc'
        if not conf.buffer or not conf.stack:
            return -1
        s = conf.stack[-1]
        b = conf.buffer.pop(0)

        conf.stack.append(b)
        conf.arcs.append((s, relation, b))

    @staticmethod
    def reduce(conf):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        #print 'reduce'
        if not conf.stack:
            return -1
        #head = false
        s = conf.stack[-1]
        if any(s == wi for wk, l, wi in conf.arcs):
            conf.stack.pop()
            return conf
        return -1
        #raise NotImplementedError('Please implement reduce!')
        #return -1

    @staticmethod
    def shift(conf):
        #print 'shift'
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        if not conf.buffer:
            return -1
        else:
            conf.stack.append(conf.buffer.pop(0))
        #raise NotImplementedError('Please implement shift!')
        #return -1
